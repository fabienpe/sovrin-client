from sovrin_client.agent.endpoint import Endpoint, ZEndpoint


class AgentNet:
    """
    Mixin for Agents to encapsulate the network interface to communicate with
    other agents.
    """
    def __init__(self, name, port, basedirpath, msgHandler, config):
        if port:
            if config.UseZStack:
                self.endpoint = ZEndpoint(port=port,
                                          msgHandler=msgHandler,
                                          name=name,
                                          basedirpath=basedirpath)
            else:
                self.endpoint = Endpoint(port=port,
                                         msgHandler=msgHandler,
                                         name=name,
                                         basedirpath=basedirpath)
        else:
            self.endpoint = None
