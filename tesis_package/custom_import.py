print("Requires Library: `subprocess'")
import subprocess
class BetterImports:
  def __init__(self, always_reimport=False, always_reinstall=False):
    """
    Initialize the DynamicImporter.

    Setup Parameters:
    - always_reimport (bool): Force reimporting even if the library or elements are already imported.
    - always_reinstall (bool): Force reinstalling the library.
    """
    self.always_reimport = always_reimport
    self.always_reinstall = always_reinstall

  def custom_install(self, library):
      subprocess.run(f'pip install {library.split(".")[0]}', shell=True, check=True)
      print(f'Library {library} installed successfully.')

  def custom_import(self, import_str, library):
      exec(import_str, globals())
      print(f'Library {library} imported successfully. As: \n {self.import_str}')

  def set_import(self, import_str):
    """
    Dynamically import and install Python libraries. It uses the configurations previously setted up when declaring the instance.

    Parameters:
    - import_str (str): The usual import statement in the format 'from library import ...' or 'import library'.
    
    """
    self.import_str = import_str
    always_reinstall = self.always_reinstall
    always_reimport = self.always_reimport

    library = import_str.split(' ')[1].strip()

    if not 'from' in import_str:
      any_not_installed = True if library not in globals() else False
      try:
        lib_custom_name = import_str.split(' ')[3].strip()
        any_not_installed = True if lib_custom_name not in globals() else False
      except IndexError:
        lib_custom_name = None
      
      output_str = lib_custom_name if lib_custom_name else library
      

    else: 
      elements_str = import_str.split('import ')[1].strip().split(',')
      elements_dic = {}
      for e in elements_str:
        name_std = e.split(' as ')[0].strip()
        try:
          name_custom = e.split(' as ')[1].strip()
        except IndexError:
          name_custom = name_std
        elements_dic[name_std] = name_custom
      any_not_installed = any(e not in globals() for e in list(elements_dic.values()))

      output_str = f'From {library}: {import_str.split("import ")[1].strip()}'
  
    if always_reinstall:
      try:
        self.custom_install(library)
        self.custom_import(import_str, library)
      except subprocess.CalledProcessError:
        print(f'Failed to install {library}')
      except ImportError as err:
        print(f'After Install. Import error: {err}')

    else:
      if always_reimport == True or any_not_installed == True:
          try:
            self.custom_import(import_str, library)
          except ImportError as err:
            print(f'Import error: {err}')
            if library in str(err):
              try:
                  # Use subprocess to run the pip install command
                  self.custom_install(library)
                  self.custom_import(import_str, library)
              except subprocess.CalledProcessError:
                  print(f'Failed to install {library}.')
      else:
        print(f'{output_str} already installed and imported')