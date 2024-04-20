class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """initializing the values."""
        self._status: bool = False
        self._muted: bool = False
        self._volume: int = Television.MIN_VOLUME
        self._channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """turn the tv on and off using status"""
        self._status = not self._status
        if not self._status:
            self._muted = False

    def mute(self) -> None:
        """when on, mute or unmute tv."""
        if self._status:
            if self._muted:
                self._muted = False
                self._volume = self._previous_volume
            else:
                self._muted = True
                self._previous_volume = self._volume
                self._volume = 0

    def channel_up(self) -> None:
        """increase the channel by 1 or set to MIN_CHANNEL if at MAX_CHANNEL"""
        if self._status:
            self._channel = (self._channel + 1) % (Television.MAX_CHANNEL + 1)

    def channel_down(self) -> None:
        """decrease the channel by 1 or set to MAX_CHANNEL if at MIN_CHANNEL."""
        if self._status:
            self._channel = (self._channel - 1) % (Television.MAX_CHANNEL + 1)

    def volume_up(self) -> None:
        """increase the volume by 1, up to MAX_VOLUME"""
        if self._status and not self._muted:
            self._volume = min(self._volume + 1, Television.MAX_VOLUME)

    def volume_down(self) -> None:
        """decrease the volume by 1, down to MIN_VOLUME."""
        if self._status and not self._muted:
            self._volume = max(self._volume - 1, Television.MIN_VOLUME)

    def __str__(self) -> str:
        """return a string of the Television object"""
        return f"Power = {self._status}, Channel = {self._channel}, Volume = {self._volume}"
