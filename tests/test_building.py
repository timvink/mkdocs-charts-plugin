"""
Test that builds with different setting succeed.

Note that pytest offers a `tmp_path`.

You can reproduce locally with:

```python
%load_ext autoreload
%autoreload 2
import os
import tempfile
import shutil
from pathlib import Path
tmp_path = Path(tempfile.gettempdir()) / 'pytest-table-builder'
if os.path.exists(tmp_path):
    shutil.rmtree(tmp_path)
os.mkdir(tmp_path)
```

"""

import pytest
import os
import shutil
import logging
from click.testing import CliRunner
from mkdocs.__main__ import build_command


def setup_clean_mkdocs_folder(mkdocs_yml_path, output_path):
    """
    Sets up a clean mkdocs directory.
    outputpath/testproject
    ├── docs/
    └── mkdocs.yml
    Args:
        mkdocs_yml_path (Path): Path of mkdocs.yml file to use
        output_path (Path): Path of folder in which to create mkdocs project
    Returns:
        testproject_path (Path): Path to test project
    """
    assert os.path.exists(mkdocs_yml_path)

    testproject_path = output_path / "testproject"

    # Create empty 'testproject' folder
    if os.path.exists(str(testproject_path)):
        logging.warning(
            """This command does not work on windows.
        Refactor your test to use setup_clean_mkdocs_folder() only once"""
        )
        shutil.rmtree(str(testproject_path))

    # Copy correct mkdocs.yml file and our test 'docs/'
    yml_dir = os.path.dirname(mkdocs_yml_path)
    shutil.copytree(yml_dir, str(testproject_path))
    shutil.copyfile(mkdocs_yml_path, str(testproject_path / "mkdocs.yml"))

    assert os.path.exists(str(testproject_path / "mkdocs.yml"))
    return testproject_path


def build_docs_setup(testproject_path):
    """
    Runs the `mkdocs build` command.
    Args:
        testproject_path (Path): Path to test project
    Returns:
        command: Object with results of command
    """
    cwd = os.getcwd()
    os.chdir(str(testproject_path))

    try:
        run = CliRunner().invoke(build_command, catch_exceptions=True)
        os.chdir(cwd)
        return run
    except:
        os.chdir(cwd)
        raise


def check_build(tmp_path, project_mkdocs, exit_code=0):
    """
    Test to make sure build fails or succeeds.
    """
    tmp_proj = setup_clean_mkdocs_folder(
        "tests/fixtures/projects/%s" % project_mkdocs, tmp_path
    )
    result = build_docs_setup(tmp_proj)

    msg = "cwd: %s, result: %s, exception: %s, exc_info: %s" % (
        os.getcwd(),
        result,
        result.exception,
        result.exc_info,
    )
    assert result.exit_code == exit_code, msg
    return tmp_proj


def test_basic_build(tmp_path):
    """
    Test.
    """
    check_build(tmp_path, "basic/mkdocs.yml")


def test_error_invalid_json(tmp_path, capsys):
    """
    Waiting for this feature.

    See https://github.com/facelessuser/pymdown-extensions/issues/1526
    """
    tmp_proj = setup_clean_mkdocs_folder(
        "tests/fixtures/projects/invalid_json/mkdocs.yml", tmp_path
    )
    result = build_docs_setup(tmp_proj)
    assert result.exit_code == 1
