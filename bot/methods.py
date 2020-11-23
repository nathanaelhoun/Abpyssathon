from discord import Message as discordMessage


def parse_mentions(message: discordMessage):
    members = set()

    for member in message.mentions:
        members.add(member)

    for role in message.role_mentions:
        for member in role.members:
            members.add(member)

    return members
