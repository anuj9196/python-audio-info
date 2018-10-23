## Python Audio Info

#### Installing
Clone the repository to your local system.   

This library is using `Pipenv Virtual Environment`.

Run below commands to installed dependencies and create a virtual environment.
```python
pipenv install
```

#### Using library
To use the library run following commands
```python
pipenv run python audio.py [<dir_path_of_mp3_files>]
```

Ex:
```python
pipenv run python audio.py music_files
```

#### Note
You can pass absolute path as well with path starting with **/**. If absolute path is not detected, it will try to 
locate the directory at the same level as of the audio.py file.

#### Author
* Anuj Sharma [http://anujsh.in](http://anujsh.in) (contact@anujsh.in)
* [http://thebornengineer.com](http://thebornengineer.com)