# -*- coding: utf-8 -*-
from typing import List

from chaoslib.discovery.discover import (discover_actions, discover_probes,
                                         initialize_discovery_result)
from chaoslib.types import DiscoveredActivities, Discovery
from logzero import logger

__version__ = '0.1.0'


def discover(discover_system: bool = True) -> Discovery:
    """
    Discover Dynatrace capabilities from this extension.
    """
    logger.info("Discovering capabilities from chaostoolkit-dynatrace")

    discovery = initialize_discovery_result(
        "chaostoolkit-dynatrace", __version__, "dynatrace")
    discovery["activities"].extend(load_exported_activities())

    return discovery


###############################################################################
# Private functions
###############################################################################
def load_exported_activities() -> List[DiscoveredActivities]:
    """
    Extract metadata from actions and probes exposed by this extension.
    """
    activities = []
    activities.extend(discover_probes("chaosdynatrace.probes"))

    return activities
