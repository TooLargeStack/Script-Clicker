import time
from multiprocessing import Process, Queue

from pynput.mouse import Listener, Button, Controller


class Test:

    def __init__(self):
        self.queue = Queue()
        self.process = Process(target=Test.click_multiple_times, args=(self.queue,))

    @staticmethod
    def click_multiple_times(queue: Queue) -> None:
        mouse = Controller()

        while True:
            mouse.click(Button.left)
            time.sleep(0.97)
            if not queue.empty() and queue.get() == 'stop':
                break

    def on_click(self, x: int, y: int, button: Button, pressed: bool):
        print('{0} at {1}'.format(
            'Pressed' if pressed else 'Released',
            (x, y)))

        if button == Button.right and pressed:
            if not self.process.is_alive():
                self.process = Process(target=self.click_multiple_times, args=(self.queue,))
            self.process.start()
        if button == Button.right and not pressed:
            self.queue.put('stop')
            self.process.join()


if __name__ == "__main__":
    with Listener(on_click=Test().on_click) as listener:
        listener.join()
