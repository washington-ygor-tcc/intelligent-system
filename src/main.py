import os
from src.applications.fastapi_factory import FastAPIFactory


class Main:
  def __init__(self):
    self.__application_type = os.environ.get('APPLICATION_TYPE')

    if self.__application_type == 'REST':
      self.__application_entrypoint = FastAPIFactory().create_entrypoint()
    else:
      raise RuntimeError('Failed to create new application, input application type not supported!')

  def run(self):
    return self.__application_entrypoint.run()


entrypoint = Main().run()
