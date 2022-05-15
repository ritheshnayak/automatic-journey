def beg(Client) -> None:
    Client.send_message("pls beg")

    latest_message = Client.retreive_message("pls beg")

    try:
        coins = int(
            "".join(
                filter(
                    str.isdigit,
                    latest_message["embeds"][0]["description"].split("**")[1],
                )
            )
        )
    except Exception:
        coins = "no"

    try:
        items = (
            latest_message["embeds"][0]["description"].split("**")[-2]
            if latest_message["embeds"][0]["description"].count("**") == 4
            else "no items"
        )
    except Exception:
        items = "no items"

    Client.log(
        "DEBUG",
        f"Received {'⏣ ' if coins != 'no' else ''}{coins} coin{'' if coins == 1 else 's'} &{' an' if items[0] in ['a', 'e', 'i', 'o', 'u'] else '' if items == 'no items' else ' a'} {items} from the `pls beg` command.",
    )
