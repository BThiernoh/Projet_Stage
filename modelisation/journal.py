import logging
import sys

def configurer_journal(niveau="INFO", fichier_log=None):
    handlers = [logging.StreamHandler(sys.stdout)]
    if fichier_log:
        handlers.append(logging.FileHandler(fichier_log, encoding="utf-8"))
    logging.basicConfig(
        level=getattr(logging, niveau.upper()),
        format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        handlers=handlers,
        force=True,
    )