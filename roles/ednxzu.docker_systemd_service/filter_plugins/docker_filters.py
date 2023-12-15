# filter_plugins/docker_filters.py

def create_docker_flags(flags):
    if flags:
        filtered_flags = [
            create_docker_flag(item) for item in flags if create_docker_flag(item)
        ]
        return "\n".join(filtered_flags)
    return None


def create_docker_flag(item):
    if isinstance(item, dict):
        key = list(item.keys())[0]
        value = item[key]
        if value is not None:
            if isinstance(value, list):
                flag_values = ['--{} "{}"'.format(key, val) for val in value]
                joined_values = " \\\n".join(flag_values)
                return f"{joined_values} \\" if joined_values else None
            else:
                return '--{} "{}" \\'.format(key, value)
    elif isinstance(item, str):
        return "--{} \\".format(item)
    return None


class FilterModule(object):
    def filters(self):
        return {
            "create_docker_flags": create_docker_flags,
        }
