# todo(obaranov) This is deprecated option. Use --inventory flag from the subcommand spec
options:
    verbose:
        help: 'Control Ansible verbosity level'
        short: v
        action: count
        default: 0
    debug:
        help: 'Run InfraRed in DEBUG mode'
        short: d
        action: store_true
    inventory:
        help: Inventory file
        type: str
        default: local_hosts
