class Strings:
    # General
    LAUNCH_SUCCESSFUL = 'Je suis vivant !'
    CONNECTION_SUCCESSFUL = 'Connecté en tant que {}'

    ERR_NO_SUBCOMMAND = ":vs: Sous-commande non valide"
    ERR_BOT_MISSING_PERMISSIONS = ":x: Je n'ai pas assez de permissions pour faire ça..."
    ERR_PRIVATE_CHANNEL = ":x: Désolé, mais je n'accepte pas les commandes depuis les messages privés ! Contacte-moi sur un serveur :wink:"
    ERR_BAD_ARGUMENTS = ":vs: Mauvais arguments passés en paramètre"
    ERR_MISSING_REQUIRED_ARGUMENT = ":x: Il manque un argument requis pour cette fonction"

    HELP = "**Menu d'aide**"

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

    RANDOM_TEAMS_PERFECT = ":white_check_mark: J'ai constitué des groupes de {} avec le rôle {}"
    RANDOM_TEAMS_TEAM_LABEL = ":diamond_shape_with_a_dot_inside: Équipe {} :"
    RANDOM_TEAMS_MEMBER_LABEL = "            :white_medium_small_square: {}"
    RANDOM_PICKONE_SUCCESS = "Et l'élu est {} !"

    # Commands group : score()
    SCORE_ADD_ERR_NAN = ":x: Ceci n'est pas un nombre de point"
    SCORE_ADD_ERR_NEGATIVE = ":x: Impossible d'ajouter un nombre négatif de point"
    SCORE_ADD_ERR_POSITIVE = ":x: Impossible de retirer un nombre positif de point"
    SCORE_ERR_DATABASE = ":x: Ajout à la base échoué"
    SCORE_ADD_SUCCESSFULLY = ":white_check_mark: J'ai bien rajouté {} points à **{}** sur ordre de _{}_."
    
    SCORE_SHOW_NO_POINTS="Rien à afficher. Vous êtes tous des élèves sages. :scream: "
    SCORE_SHOW_RANKING_INTRO=":trophy: Et voici le classement des points de int "
    SCORE_SHOW_RANKING_ITEM="#{} : {} ({} points)"
    SCORE_SHOW_MEMBER_HAS_LEFT="_a quitté le serveur_"