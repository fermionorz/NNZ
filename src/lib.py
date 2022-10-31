import os
import toml


def get_runs_config():
    path = "res/common_tools"
    config = []
    for v in os.listdir(path):
        app_exec = f"res\\common_tools\\{v}\\{v}.bat"   # 启动脚本
        app_img = f"res/common_tools/{v}/{v}.png"       # logo
        config.append((v, app_exec, app_img))
    return config


def get_env(env_path=f"res/env/env.toml"):
    config = toml.load(env_path)
    return config


def get_terminal_tools_config(terminal_tools_path=f"res/terminal_tools"):
    env_config = get_env()
    config = []

    for v in os.listdir(terminal_tools_path):
        config.append(toml.load(f"{terminal_tools_path}/{v}/{v}.toml"))

    for v in config:
        if v['ppname'] == 'None':
            run_cmd = f"{terminal_tools_path}/{v['name']}/{v['pname']}"
        else:
            run_cmd = f"{env_config[v['ppname']]} {terminal_tools_path}/{v['name']}/{v['pname']}"
        v['run_cmd'] = run_cmd

        option_args, input_args = 'option_args', 'input_args'
        if option_args in v:
            for vv in v[option_args]:
                vv['arg_more'] += f"({vv['arg_name'].replace(' ', '')})"

        if input_args in v:
            for vv in v[input_args]:
                vv['arg_more'] += f"({vv['arg_name'].replace(' ', '')})"
    return config


def get_other_tools_config(path="res/other_tools/"):

    try:
        other_tools = os.listdir(path)
    except:
        os.mkdir(path)
    configs = {}
    for i in other_tools:
        temp = os.listdir(path+i)
        configs[i] = temp
    return configs


if __name__ == '__main__':
    res = get_other_tools_config(path="../res/other_tools/")

    print(res)
