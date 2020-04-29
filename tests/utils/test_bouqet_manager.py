import pytest

from bloomon.utils.bouqet_manager import BouqetManager


def test_add_bouqet_design_to_manager_with_correct_name():
    """
    Testing size of the internal list of designs
    """
    # given
    manager = BouqetManager()

    # when
    manager.addBouqetDesign("AL8d10r5t30")

    # then
    assert len(manager.getDesigns()) == 1


def test_get_bouqet_design_name_and_size_with_basic_name():
    """
    Testing basic properties of the bouqet design
    """

    # given
    manager = BouqetManager()

    # when
    manager.addBouqetDesign("AL8d10r5t30")
    design = manager.getDesigns()[0]

    # then
    assert design.getName() == 'A'
    assert design.getSize() == 'L'
    assert design.getFlowersQuantity() == 30


correct_testdata = [
    ("AL8d10r5t3", 3),
    ("AL8d10r5t30", 30),
    ("AL8d10r5t300", 300),
    ("AL8d10r5t30000", 30000),
    ("AL8d10r5t67", 67)
]


@pytest.mark.parametrize("name, expected", correct_testdata)
def test_different_bouqet_design_sizes_when_assign_to_them_different_names(name, expected):
    """
    Testing different correct design names
    """

    # given
    manager = BouqetManager()

    # when
    manager.addBouqetDesign(name)
    design = manager.getDesigns()[0]

    # then
    assert design.getFlowersQuantity() == expected


incorrect_testdata = [
    ("AL8d10r5t0", 0),
    ("AL8d10r5t", 0)
]


@pytest.mark.parametrize("name, expected", incorrect_testdata)
def test_different_bouqet_design_sizes_when_assign_to_them_wrong_names(name, expected):
    """
    Testing different wrong design names
    """

    # given
    manager = BouqetManager()

    # when
    # then
    with pytest.raises(RuntimeError, match=r".* does not have .*"):
        manager.addBouqetDesign(name)


correct_flowers_testdata = [
    ("AL8d10r5t3", {'d': 8, 'r': 10, 't': 5}),
    ("AL88c140r57t3", {'c': 88, 'r': 140, 't': 57}),
    ("AL88c140r57y97j6444k12t3", {'c': 88, 'r': 140, 'y': 57, 'j': 97, 'k': 6444, 't': 12}),
]


@pytest.mark.parametrize("name, expected", correct_flowers_testdata)
def test_different_flowers_in_the_bouqet_design_when_adding_correct_name(name, expected):
    """
    Testing flowers in the design
    """

    # given
    manager = BouqetManager()

    # when
    manager.addBouqetDesign(name)
    design = manager.getDesigns()[0]

    # then
    assert design.getFlowers() == expected
