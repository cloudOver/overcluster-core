MODULE = {
    'models': ['corecluster.models.core'],
    'api': [
        'corecluster.views.admin',
        'corecluster.views.api',
        'corecluster.views.user',
    ],
    'ci': [
        'corecluster.views.ci',
    ],
    'configs': {
        'core': '/etc/corecluster/config.py',
        'hardware': '/etc/corecluster/hardware.py',
        'agent': '/etc/corecluster/agent.py',
    },
    'hooks': {
        'agent.vm.create': ['corecluster.hooks.vm'],
        'agent.vm.remove_vm': ['corecluster.hooks.vm'],
        'cron.minute': ['corecluster.hooks.node_libvirt', 'corecluster.hooks.wakeonlan'],
        'cron.hourly': ['corecluster.hooks.vm_cleanup_db', 'corecluster.hooks.vm_cleanup_task'],
        'cron.daily': [],
    },
    'agents': [
        {'type': 'vm', 'module': 'corecluster.agents.vm', 'count': 4},
        {'type': 'network', 'module': 'corecluster.agents.network', 'count': 4},
        {'type': 'console', 'module': 'corecluster.agents.console', 'count': 1}
    ],
    'drivers': {

    },
    'algorithms': {

    },
    'cli': {
        'agent': 'corecluster.cli.agent',
        'api': 'corecluster.cli.api',
        'image': 'corecluster.cli.image',
        'network_pool': 'corecluster.cli.network_pool',
        'node': 'corecluster.cli.node',
        'storage': 'corecluster.cli.storage',
        'subnet': 'corecluster.cli.subnet',
        'task': 'corecluster.cli.task',
        'vm': 'corecluster.cli.vm',
    }
}
