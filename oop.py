from abc import ABC, abstractmethod


class MusicLibraryItem(ABC):
    def __init__(self, title: str, artist: str):
        self._title = title
        self._artist = artist
        self._is_available = True

    @abstractmethod
    def item_type(self) -> str:
        pass

    def check_out(self) -> bool:
        if self._is_available:
            self._is_available = False
            return True
        return False

    def return_item(self) -> None:
        self._is_available = True

    def get_info(self) -> str:
        availability = 'Available' if self._is_available else 'Checked out'
        return f'{self.item_type()} - {self._title} by {self._artist} ({availability})'


class Track(MusicLibraryItem):
    def __init__(self, title: str, artist: str, genre: str):
        super().__init__(title, artist)
        self._genre = genre

    def item_type(self) -> str:
        return 'Track'

    def get_genre(self) -> str:
        return self._genre


class Album(MusicLibraryItem):
    def __init__(self, title: str, artist: str, release_year: int):
        super().__init__(title, artist)
        self._release_year = release_year

    def item_type(self) -> str:
        return 'Album'

    def get_release_year(self) -> int:
        return self._release_year


class MusicListener:
    _total_listeners = 0

    def __init__(self, name: str):
        self._name = name
        self._borrowed_items = []
        MusicListener._total_listeners += 1

    @classmethod
    def total_listeners(cls) -> int:
        return cls._total_listeners

    def borrow_item(self, item: MusicLibraryItem) -> bool:
        if item.check_out():
            self._borrowed_items.append(item)
            return True
        return False

    def return_item(self, item: MusicLibraryItem) -> None:
        if item in self._borrowed_items:
            item.return_item()
            self._borrowed_items.remove(item)

    def get_borrowed_items_info(self) -> str:
        info = [item.get_info() for item in self._borrowed_items]
        return '\n'.join(info) if info else 'No borrowed items.'


if __name__ == "__main__":
    track1 = Track("Bohemian Rhapsody", "Queen", "Rock")
    album1 = Album("Dark Side of the Moon", "Pink Floyd", 1973)
    listener1 = MusicListener("Alice")
    listener2 = MusicListener("Bob")

    print(listener1.borrow_item(track1))
    print(listener1.get_borrowed_items_info())
    print(listener2.borrow_item(album1))
    print(listener2.get_borrowed_items_info())
    print("Total listeners:", MusicListener.total_listeners())
