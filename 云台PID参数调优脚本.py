import numpy as np
import matplotlib.pyplot as plt
'''
功能描述
通过Ziegler-Nichols方法自动计算PID参数
模拟云台控制系统响应
可视化调优效果
'''
class PIDController:
    def __init__(self, Kp, Ki, Kd):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.prev_error = 0
        self.integral = 0

    def compute(self, setpoint, measured_value):
        error = setpoint - measured_value
        self.integral += error
        derivative = error - self.prev_error
        output = self.Kp * error + self.Ki * self.integral + self.Kd * derivative
        self.prev_error = error
        return output

def simulate_pid(Kp, Ki, Kd):
    pid = PIDController(Kp, Ki, Kd)
    setpoint = 50  # 目标位置
    measured_value = 0  # 初始位置
    time = np.arange(0, 10, 0.1)
    positions = []
    
    for t in time:
        control = pid.compute(setpoint, measured_value)
        measured_value += control * 0.1  # 模拟系统响应
        positions.append(measured_value)
    
    plt.plot(time, positions, label=f'Kp={Kp}, Ki={Ki}, Kd={Kd}')
    plt.xlabel('Time')
    plt.ylabel('Position')
    plt.legend()

# Ziegler-Nichols参数调优
Ku = 3.2  # 临界增益
Tu = 0.8  # 临界周期
Kp = 0.6 * Ku
Ki = 1.2 * Ku / Tu
Kd = 0.075 * Ku * Tu

# 测试不同参数
simulate_pid(Kp, 0, 0)  # 仅比例控制
simulate_pid(Kp, Ki, 0)  # PI控制
simulate_pid(Kp, Ki, Kd)  # PID控制
plt.title('云台PID参数调优')
plt.show()