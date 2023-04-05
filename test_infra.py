import pytest
import tftest
import json

from pathlib import Path


@pytest.fixture
def plan():
    file_path = Path(__file__).resolve()
    base_dir = file_path.parent.absolute()
    tf = tftest.TerraformTest(tfdir=".", basedir=base_dir)
    tf.setup()
    return tftest.TerraformPlanOutput(tf.plan(output=True))


def test_outputs(plan):
    """Simple test of the changes after a terraform plan cmd
    """
    address = 'docker_container.nginx'
    change = plan.resource_changes[address]
    assert change['address'] == address
    assert change['change']['before'] is None
