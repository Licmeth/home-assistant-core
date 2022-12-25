"""Support for Kostal Piko solar power inverter."""
from __future__ import annotations

import logging

from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

from .const import DATA_CONFIG, DOMAIN

_LOGGER = logging.getLogger(__name__)


async def async_setup(hass: HomeAssistant, yaml_config: ConfigType) -> bool:
    """Activate Google Actions component."""
    if DOMAIN not in yaml_config:
        return True

    hass.data[DOMAIN] = {}
    hass.data[DOMAIN][DATA_CONFIG] = yaml_config[DOMAIN]

    return True
