import argparse

from plotmanager.library.utilities.exceptions import InvalidArgumentException
from plotmanager.library.utilities.commands import start_manager, stop_manager, view, analyze_logs, view_history, kill_job


parser = argparse.ArgumentParser(description='This is the central manager for Swar\'s Chia Plot Manager.')

help_description = '''
There are a few different actions that you can use: "start", "restart", "stop", "view", and "analyze_logs". "start" will 
start a manager process. If one already exists, it will display an error message. "restart" will try to kill any 
existing manager and start a new one. "stop" will terminate the manager, but all existing plots will be completed. 
"view" can be used to display an updating table that will show the progress of your plots. Once a manager has started it 
will always be running in the background unless an error occurs. This field is case-sensitive.

"analyze_logs" is a helper command that will scan all the logs in your log_directory to get your custom settings for
the progress settings in the YAML file.
'''

def restart(args):
    stop_manager(args)
    start_manager(args)

subparsers = parser.add_subparsers()

parser_start = subparsers.add_parser('start', help='starts the Swar manager')
parser_start.set_defaults(func=start_manager)

parser_restart = subparsers.add_parser('restart', help='restarts the Swar manager')
parser_restart.set_defaults(func=restart)

parser_stop = subparsers.add_parser('stop', help='stops the Swar manager')
parser_stop.set_defaults(func=stop_manager)

parser_view = subparsers.add_parser('view', help='views the current jobs')
parser_view.set_defaults(func=view)

parser_analyze_logs = subparsers.add_parser('analyze_logs', help='analyzes the logs')
parser_analyze_logs.set_defaults(func=analyze_logs)

parser_history = subparsers.add_parser('history', help='shows job history')
parser_history.set_defaults(func=view_history)

parser_kill = subparsers.add_parser('kill', help='kills a job')
parser_kill.add_argument('pid', type=int, default=-1)
parser_kill.add_argument('--delete-temp-files', '-d', action='store_true', default=False, help='deletes the temporary files associated with the PID')
parser_kill.set_defaults(func=kill_job)

args = parser.parse_args()

try:
    args.func(args)
except AttributeError:
    parser.print_help()
