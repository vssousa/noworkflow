# Copyright (c) 2016 Universidade Federal Fluminense (UFF)
# Copyright (c) 2016 Polytechnic Institute of New York University.
# This file is part of noWorkflow.
# Please, consult the license terms in the LICENSE file.
"""Module Dependency Model"""
from __future__ import (absolute_import, print_function,
                        division, unicode_literals)

from sqlalchemy import Column, Integer
from sqlalchemy import ForeignKeyConstraint, PrimaryKeyConstraint

from ...utils.prolog import PrologDescription, PrologTrial, PrologAttribute
from ...utils.prolog import PrologRepr, PrologNullableRepr

from .base import AlchemyProxy, proxy_class, one, backref_one


@proxy_class
class ModuleDependency(AlchemyProxy):
    """Represent a Module Dependency"""

    __tablename__ = "module_dependency"
    __table_args__ = (
        PrimaryKeyConstraint("trial_id", "module_id"),
        ForeignKeyConstraint(["trial_id"], ["trial.id"], ondelete="CASCADE"),
        ForeignKeyConstraint(["module_id"], ["module.id"], ondelete="CASCADE"),
    )
    trial_id = Column(Integer, nullable=False, index=True)
    module_id = Column(Integer, nullable=False, index=True)

    module = one("Module")

    trial = backref_one("trial")  # Trial.dmodule_dependencies

    prolog_description = PrologDescription("module", (
        PrologTrial("trial_id", link="trial.id"),
        PrologAttribute("id", attr_name="module.id"),
        PrologRepr("name", attr_name="module.name"),
        PrologNullableRepr("version", attr_name="module.version"),
        PrologNullableRepr("path", attr_name="module.path"),
        PrologNullableRepr("code_hash", attr_name="module.code_hash"),
    ), description=(
        "informs that a given trial (*TrialId*)\n"
        "imported the *version* of a module (*Id*) with *Name*,\n"
        "and content (*CodeHash*) written in *Path*."
    ))

    def __repr__(self):
        return self.prolog_description.fact(self)
