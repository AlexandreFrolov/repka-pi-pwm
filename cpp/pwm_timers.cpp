#include <iostream>
#include <fstream>
#include <chrono>
#include <future>

const int servo_pin = 8;
const int frequency_Hz = 50;
const float pulse_duration_ms = 1.5;

std::atomic<bool> should_exit(false);

void set_gpio_value(int value) {
    std::ofstream gpio_value_file("/sys/class/gpio/gpio" + std::to_string(servo_pin) + "/value");
    gpio_value_file << value;
    gpio_value_file.close();
}

void generate_pulse(int pulse_duration_us) {
    set_gpio_value(1);
    std::this_thread::sleep_for(std::chrono::microseconds(pulse_duration_us));
    set_gpio_value(0);
}

void pulse_function() {
    float dutyCycle = 90 / 18.0f + 3.0f;
    float period_duration = (1000.0f / 50) * 1000;
    float pulse_duration = static_cast<int>(period_duration * (dutyCycle / 100.0f));
    int pulse_duration_us = static_cast<int>(pulse_duration_ms * 1000);
    int wait_after_pulse = static_cast<int>(period_duration - pulse_duration_us);

    std::cout << "wait_after_pulse: " << wait_after_pulse << " ms" << std::endl;
    std::cout << "pulse_duration: " << pulse_duration << " us" << std::endl;
    std::cout << "pulse_duration_us: " << pulse_duration_us << " us" << std::endl;
    std::cout << "dutyCycle: " << dutyCycle << std::endl;
    std::cout << "period_duration: " << period_duration << " ms" << std::endl;

    while (!should_exit) {
        auto pulse_task = std::async(std::launch::async, generate_pulse, pulse_duration_us);
        pulse_task.wait();
        std::this_thread::sleep_for(std::chrono::microseconds(wait_after_pulse));
    }
}

int main() {
    try {
        std::ofstream gpio_export_file("/sys/class/gpio/export");
        gpio_export_file << servo_pin;
        gpio_export_file.close();

        std::ofstream gpio_direction_file("/sys/class/gpio/gpio" + std::to_string(servo_pin) + "/direction");
        gpio_direction_file << "out";
        gpio_direction_file.close();

        std::thread pulse_thread(pulse_function);
        std::this_thread::sleep_for(std::chrono::seconds(10));

        should_exit = true;
        pulse_thread.join();

        std::ofstream gpio_unexport_file("/sys/class/gpio/unexport");
        gpio_unexport_file << servo_pin;
        gpio_unexport_file.close();
		} catch (const std::exception& e) {
			std::cerr << "Exception: " << e.what() << "\n";
    }

    return 0;
}
