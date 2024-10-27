import asyncio

from bot import TeleBot


class TrafficBot:
    bot: TeleBot

    def __init__(self):
        self.bot = TeleBot()

    def run(self):
        try:
            asyncio.run(self._run())
        except Exception as e:
            print(f'Critical error: {e}')

    async def _run(self):
        print('Bot started')


if __name__ == '__main__':
    TrafficBot().run()
