import logging

def configure_rotating_logger(logger_name,log_filepath,max_size_bytes,backup_count):
  
    if not logger_name or not log_filepath:
        raise ValueError("string cant be empty")
    
    if not isinstance(logger_name,str) or not isinstance(log_filepath,str):
        raise TypeError("not  a valid string")
    
    max_size_bytes=int(max_size_bytes)
    if max_size_bytes <= 0:
        raise ValueError(f"{max_size_bytes} cant be less than 0")
    
    backup_count=int(backup_count)
    if backup_count < 0:
        raise ValueError(f"{backup_count} cant be negative")
    
    logger=logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
      
    handler=logging.RotatingFileHandler(
            log_filepath,
            maxBytes=max_size_bytes,
            backupCount=backup_count
    )
    formatter=logging.Formatter(
              "%(asctime)s-%(levelname)s-%(messages)"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
    
    

    
    
    
