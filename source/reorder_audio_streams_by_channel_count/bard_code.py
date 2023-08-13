import unmanic


class ChannelOrderPlugin(unmanic.Plugin):
    def __init__(self):
        super().__init__()

    def process(self, tracks):
        tracks.sort(key=lambda track: track.channels)


if __name__ == "__main__":
    plugin = ChannelOrderPlugin()
    plugin.run()





import unmanic

class ChannelSorter(unmanic.Plugin):
    def __init__(self):
        super().__init__()

    def process(self, streams):
        streams.sort(key=lambda stream: stream.channels, reverse=True)

        return streams

unmanic.register_plugin(ChannelSorter)

#Best????
import unmanic

class ChannelSorter(unmanic.Plugin):
    def __init__(self):
        super().__init__()

    def process(self, streams):
        streams.sort(key=lambda stream: stream.channels, reverse=True)

        return streams


unmanic.register_plugin(ChannelSorter)
