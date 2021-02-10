# pylint: disable=R


class Pluralizer:
    """Simple pluralization of a string. Use with .format and {:N point/s}"""

    def __init__(self, value):
        self.value = value

    def __format__(self, formatter):
        formatter = formatter.replace("N", str(self.value))
        start, _, suffixes = formatter.partition("/")
        singular, _, plural = suffixes.rpartition("/")

        return "{}{}".format(start, singular if abs(self.value) < 2 else plural)


class Strings:
    """Strings used in the message sent"""

    # Category emojis
    EM_FATAL = ":x: "
    EM_WARN = ":warning: "
    EM_OK = ":ok: "
    EM_SUCCESS = ":white_check_mark: "

    ERR_NO_COMMAND = "Cette commande n'existe pas. Tapez `&help` et je vous aiderai !"
    ERR_NO_SUBCOMMAND = EM_WARN + "Sous-commande non valide"
    ERR_BOT_MISSING_PERMISSIONS = (
        EM_FATAL + "Je n'ai pas assez de permissions pour faire ça..."
    )
    ERR_PRIVATE_CHANNEL = (
        EM_FATAL
        + "Désolé, mais je n'accepte pas les commandes depuis les messages privés ! "
        + "Contacte-moi sur un serveur :wink:"
    )
    ERR_BAD_ARGUMENTS = EM_WARN + "Mauvais arguments passés en paramètre"
    ERR_MISSING_REQUIRED_ARGUMENT = (
        EM_FATAL + "Il manque un argument requis pour cette fonction"
    )
    ERR_DATABASE = (
        EM_FATAL + "Impossible de me connecter à ma base de données, désolé..."
    )

    # Function : fun.ping()
    PING = "Pong ! :ping_pong:"

    # Function : fun.ping2()
    PING2 = "Pong <@199621995913150464> ! <:medhiblond:751515008877330443> :ping_pong:"

    # Function : fun.activity()
    ACTIVITY_NEW = (
        EM_OK + "Je suis maintenant en train de jouer à **{}** sur ordre de _{}_"
    )

    # Function : utilities.archivechat()
    ARCHIVE_BEGIN = "--- Beginning archiving of channel {} (guild : {})"
    ARCHIVE_NOTIF_BEGIN = "Je commence à archiver ce canal, une seconde..."
    ARCHIVE_FILE_HEADER = "Guild : {} \nChannel : #{} \nArchive created on {} \n"
    ARCHIVE_FILE_FOOTER = "Archive end\n"
    ARCHIVE_COMPLETED = "--- Archive of #{} (guild : {}) completed"

    ARCHIVE_SUCCESS = EM_OK + "Archive du channel bien envoyée par message privé à {}"
    ARCHIVE_MESSAGE = EM_OK + "Archive du channel #{} (Serveur {})"
    ARCHIVE_FILENAME = "Archive-channel-{}-of-{}.txt"

    ARCHIVE_ERR_SENDING = EM_FATAL + "Impossible d'envoyer l'archive :sob:"

    # Command groupe : roles()
    ROLE_CREATE_SUCCESS = (
        EM_SUCCESS + "Nouveau rôle *{}* créé par _{}_ et ajouté à *{}*"
    )
    ROLE_CREATE_ERR_PERMISSION = (
        EM_FATAL + "Je n'ai pas les permissions pour créer un rôle :sob:"
    )
    ROLE_CREATE_ERR_HTTP = EM_FATAL + "Je n'ai pas réussi à créer le rôle... :cry:"
    ROLE_CREATE_INVALID_ARG = EM_FATAL + "Hum, un de ces arguments ne convient pas..."
    ROLE_CREATE_ERR_ADDED = (
        EM_WARN + "Le rôle n'a pas été ajouté à tous les membres demandés, déso."
    )
    ROLE_CREATE_ERR_EXISTING = EM_WARN + "Le rôle {} existe déjà, la preuve!"

    ROLE_SHOW_TEXT = ":label: Il y a un total de {:N rôle/s} sur ce serveur !"
    ROLE_SHOW_INTRO = (
        ""
        + "|==============================|=======|=======|\n"
        + "|             Nom              | Total |Uniques|\n"
        + "|==============================|=======|=======|\n"
    )
    ROLE_SHOW_ITEM = "|{:30s}|{:7d}|{:7d}|"

    # Commands group : utilities.random()
    RANDOM_ERR_WRONG_NB_PER_TEAM = (
        EM_WARN
        + "Tu crois vraiment qu'on va faire des équipes avec **{:N personne/s}** dans chaque ? :P "
    )

    RANDOM_TEAMS_PERFECT = EM_SUCCESS + "J'ai constitué des groupes de {} avec {}"
    RANDOM_TEAMS_TEAM_LABEL = ":game_die: Équipe {} :"
    RANDOM_TEAMS_MEMBER_LABEL = ":white_medium_small_square: {}"
    RANDOM_PICKONE_SUCCESS = "Et l'élu est {} !"

    # Commands group : score()
    SCORE_ADD_ERR_NAN = EM_FATAL + "Ceci n'est pas un nombre de point"
    SCORE_ADD_ERR_NEGATIVE = (
        EM_FATAL + "Impossible d'ajouter un nombre négatif de point"
    )
    SCORE_ADD_ERR_POSITIVE = (
        EM_FATAL + "Impossible de retirer un nombre positif de point"
    )
    SCORE_ADD_SUCCESS = (
        EM_SUCCESS + "J'ai bien rajouté {:N point/s} à **{}** sur ordre de _{}_."
    )
    SCORE_REMOVE_SUCCESS = (
        EM_SUCCESS + "J'ai bien retiré {:N point/s} à **{}** sur ordre de _{}_."
    )

    SCORE_SHOW_NO_POINTS = "Rien à afficher. Vous êtes tous des élèves sages. :scream: "
    SCORE_SHOW_RANKING_INTRO = ":trophy: Et voici le classement des points de int :"
    SCORE_SHOW_RANKING_ITEM = "#{} : {} ({:N point/s})"
    SCORE_SHOW_MEMBER_HAS_LEFT = "*a quitté le serveur*"
