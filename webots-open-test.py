import subprocess

commands = [
    "webots",
    "--batch",
    "--no-sandbox",
    "--stderr",
    '--stream="port=4000"',
    "/home/jelgar/Documents/uni/robotics/robo-gen/webots/worlds/labsheet_x.wbt",
]

subprocess.Popen(commands)
