from pypresence import Presence

RCP = Presence("1250418534245339250")
RCP.connect()
def create_Presence(title):
    RCP.update(
        state=title,
        large_image="icon",
        small_image="icon",
        instance=True
    )