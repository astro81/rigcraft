let
  	nixpkgs = fetchTarball "https://github.com/NixOS/nixpkgs/tarball/nixos-24.05";
  	pkgs = import nixpkgs { config = {}; overlays = []; };
in

pkgs.mkShellNoCC {
  	packages = with pkgs; [
  	  	python312
  	  	poetry
  	  	nodejs_22
  	];

  	MESSAGE = "Welcome to the Nix Shell Environment for your Django project in ${toString (builtins.getEnv "PWD")}";

  	#! Additional dependencies for the project
  	DEPENDENCIES = "django icecream djangorestframework django-cors-headers pillow djangorestframework-simplejwt";

  	shellHook = ''
  	  	echo "$MESSAGE"
  	  	echo "Python Version: $(python --version)"
  	  	echo "Poetry Version: $(poetry --version)"

  	  	# Generate pyproject.toml with Django and icecream during the first shell entry
  	  	if [ ! -f backend/pyproject.toml ]; then
  	  	  	printf "\nNo pyproject.toml found. Initializing a new Poetry project...\n\n"
  	  	  	poetry init \
  	  	  	  	--name "$(basename $PWD)" \
  	  	  	  	--description "A Django project" \
  	  	  	  	--author "$(basename $USER)" \
  	  	  	  	--python "^3.12" \
  	  	  	  	--no-interaction

  	  	  	# Add dependencies from the DEPENDENCIES string
  	  	  	for dep in $DEPENDENCIES; do
  	  	  	  	poetry add "$dep"
  	  	  	done

  	  	  	poetry install
  	  	  	printf "\nPoetry project initialized with dependencies: $DEPENDENCIES!\n"
  	  	else
  	  	  	echo "pyproject.toml already exists. Skipping initialization."
  	  	fi

  	  	#! Aliases
  	  	alias prp='poetry run python'
  	  	alias prd='poetry run django-admin'

  	  	alias papp='poetry run python manage.py startapp'
  	  	alias pmakemigrations='poetry run python manage.py makemigrations'
  	  	alias pmigrate='poetry run python manage.py migrate'
  	  	alias pstart='poetry run python manage.py runserver'

  	  	alias pup='poetry update'
  	  	alias pbuild='poetry build'
  	  	alias prun='poetry run'
  	  	alias pshell='poetry shell'
  	  	alias pinst='poetry install'
  	  	alias ptest='poetry run pytest'
  	'';
}
