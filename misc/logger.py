import logging

logger = logging.getLogger("discord")


def debug(message: str, path: str) -> None:
	logger.name = path
	logger.debug(message)


def info(message: str, path: str) -> None:
	logger.name = path
	logger.info(message)


def warning(message: str, path: str) -> None:
	logger.name = path
	logger.warning(message)


def error(message: str, path: str) -> None:
	logger.name = path
	logger.error(message)


def critical(message: str, path: str) -> None:
	logger.name = path
	logger.critical(message)
