import os
from github import Github, GithubException

abs = os.path.abspath( '' )

TOKEN = os.getenv( "TOKEN" );

TAG = os.getenv( "TAG" );

USER = os.getenv( "USER" );

REPOSITORY = os.getenv( "REPOSITORY" );

WIN32 = True if os.path.exists( "{}/projects/".format( abs ) ) else False;

print( "Updating Release tag \"{}\"".format( TAG ) );

try:

    g = Github( TOKEN );

    repo = g.get_repo( f'{USER}/{REPOSITORY}' );

    release = repo.create_git_release( TAG, f"# {TAG}", '', False, False );

    release.upload_asset( "{}/projects/vs2019/Release/hldll/hl.dll".format( abs ), label='hl.dll' );
    release.upload_asset( "{}/projects/vs2019/Release/hl_cdll/client.dll".format( abs ), label='client.dll' );

except GithubException as e:

    if e.status == 422:

        print( f'WARNING! tag {TAG} Already exists. Update the enviroment variable "TAG" in the workflow.' );

    print(e);

    exit(1);
