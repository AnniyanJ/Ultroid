import base64
from . import ultroid_cmd

@ultroid_cmd(pattern="decode64 ?(.*)")
async def base64_decode(event):
    if not event.pattern_match.group(1):
        await event.reply("Please provide a Base64 encoded string to decode.")
        return
    encoded_data = event.pattern_match.group(1)
    
    try:
        decoded_data = base64.b64decode(encoded_data).decode("utf-8")
        await event.reply(f"Decoded data: `{decoded_data}`")
    except Exception as e:
        await event.reply(f"Error while decoding: {str(e)}")
