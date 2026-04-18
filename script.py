import asyncio
import serial
from winsdk.windows.media.control import GlobalSystemMediaTransportControlsSessionManager as MediaManager

ser = serial.Serial('COM6', 9600)  # zamień na swój port

async def send_now_playing():
    manager = await MediaManager.request_async()
    session = manager.get_current_session()
    if not session:
        return
    info = await session.try_get_media_properties_async()
    title = info.title
    artist = info.artist
    data = f"{title} - {artist}\n"
    print(title)
    print(artist)
    ser.write(data.encode())

async def main():
    while True:
        await send_now_playing()
        await asyncio.sleep(2)

asyncio.run(main())
