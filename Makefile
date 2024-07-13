debug_on_phone:
	pipenv run buildozer -v android debug deploy run logcat

build_package:
	buildozer -v android debug

buildozer_clean:
	buildozer android clean

delete_venv:
	pipenv --rm
