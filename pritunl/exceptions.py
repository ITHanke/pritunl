class StopServer(Exception):
    pass


class BaseError(Exception):
    def __init__(self, message, data=None):
        if data:
            self.__dict__.update(data)
            message = '%s. %r' % (message, data)
        Exception.__init__(self, message)


class UserError(BaseError):
    pass

class KeyLinkError(UserError):
    pass


class EmailError(BaseError):
    pass

class EmailNotConfiguredError(BaseError):
    pass

class EmailFromInvalid(EmailError):
    pass

class EmailAuthInvalid(EmailError):
    pass


class HostError(BaseError):
    pass


class ServerError(BaseError):
    pass

class ServerInstanceSet(ServerError):
    pass

class ServerMissingOrg(ServerError):
    pass

class ServerStartError(ServerError):
    pass

class ServerStopError(ServerError):
    pass

class ServerLinkError(ServerError):
    pass

class ServerLinkOnlineError(ServerError):
    pass

class ServerLinkCommonHostError(ServerError):
    pass

class ServerLinkReplicaError(ServerError):
    pass

class IptablesError(ServerError):
    pass

class InvalidStaticFile(ServerError):
    pass

class ServerNetworkLocked(ServerError):
    pass


class NotFound(BaseError):
    pass


class QueueError(BaseError):
    pass

class QueueTimeout(QueueError):
    pass

class QueueTaskError(QueueError):
    pass

class QueueStopped(QueueError):
    pass
