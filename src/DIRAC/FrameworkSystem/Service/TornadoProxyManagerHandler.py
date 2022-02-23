""" TornadoProxyManager is the implementation of the ProxyManagement service in HTTPS

    .. literalinclude:: ../ConfigTemplate.cfg
      :start-after: ##BEGIN ProxyManager:
      :end-before: ##END
      :dedent: 2
      :caption: ProxyManager options
"""
from DIRAC.Core.Tornado.Server.TornadoService import TornadoService
from DIRAC.FrameworkSystem.Service.ProxyManagerHandler import ProxyManagerHandlerMixin


class TornadoProxyManagerHandler(ProxyManagerHandlerMixin, TornadoService):
    pass
