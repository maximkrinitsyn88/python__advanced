app_logger_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'base': {
            'format': '%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s',
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'base',
        },
        'file': {
            'class': 'logging.FileHandler',
            'level': 'DEBUG',
            'formatter': 'base',
            'filename': 'log.log',
            'mode': 'a'
        },
        'file_errors': {
            'class': 'logging.FileHandler',
            'level': 'ERROR',
            'formatter': 'base',
            'filename': 'error.log',
            'mode': 'a'
        },
        'file_info': {
            'class': 'logging.FileHandler',
            'level': 'INFO',
            'formatter': 'base',
            'filename': 'info.log',
            'mode': 'a'
        },
        'file_utils': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'h',
            'interval': 10,
            'backupCount': 5,
            'formatter': 'base',
            'filename': 'utils_log.log',
            'level': 'INFO'
        },
        'http': {
            "class": "logging.handlers.HTTPHandler",
            "level": "DEBUG",
            "formatter": "base",
            "host": '127.0.0.1:5000',
            'url': '/server_logs',
            'method': 'POST'
        },
    },
    'loggers': {
        'app_logger': {
            'level': 'DEBUG',
            'handlers': ['file', 'file_info', 'file_errors', 'console', 'http']
        },
        'utils_logger': {
            'level': 'INFO',
            'handlers': ['file_utils', 'file_info', 'file_errors', 'console', 'http']
        },
    },
}
