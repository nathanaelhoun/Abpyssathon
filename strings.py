class Strings:
    # General
    LAUNCH_SUCCESSFUL = 'Je suis vivant !'
    CONNECTION_SUCCESSFUL = 'Connecté en tant que {}'

    ERR_PRIVATE_CHANNEL = ":x: Désolé, mais je n'accepte pas les commandes depuis les messages privés ! Contacte-moi sur un serveur :wink:"
    ERR_NO_SUBCOMMAND = ":vs: Sous-commande non valide"

    # Function : fun.ping()
    PING = "Pong ! :ping_pong:"

    # Function : utilities.archivechat()
    ARCHIVE_BEGIN = '--- Archive beginning of channel {} (guild : {})'
    ARCHIVE_FILE_HEADER = "Guild : {} \nChannel : #{} \nArchive created on {} \n"
    ARCHIVE_FILE_FOOTER = "Archive ended\n"
    ARCHIVE_COMPLETED = '--- Archive completed of #{} (guild : {})"'
    
    ARCHIVE_SEND_SUCCESSFUL = ":ok: Archive du channel #{}"
    ARCHIVE_SEND_FILENAME = "Archive-channel-{}.txt"

    ARCHIVE_ERR_ATTACHMENT = ":x: Impossible d'attacher le fichier archive de #{} :sob:"
    ARCHIVE_ERR_SENDING = ":x: Impossible d'envoyer l'archive :sob:"
    ARCHIVE_ERR = ":x: Impossible de créer l'archive :sob:"

    # Commands group : utilities.random()
    RANDOM_ERR_WRONG_NUMBER_IN_TEAM = ":vs: Tu crois vraiment qu'on va faire des équipes avec **{}** personne dans chaque ? :P "
