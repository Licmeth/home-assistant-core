"""Platform for Kostal Piko sensors."""
from __future__ import annotations

import logging

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import UnitOfPower
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    """Add Kostal Piko sensors."""
    entities: list[SensorEntity] = []
    async_add_entities(entities)


class PikoDataSensor(SensorEntity):
    """Representation of a Kostal Piko data sensor."""

    _attr_has_entity_name = True

    def __init__(self, name: str) -> None:
        """Initialize the entity."""
        self._attr_name = name
        self._attr_available = False
        self._attr_device_class = SensorDeviceClass.POWER
        self._attr_native_unit_of_measurement = UnitOfPower.WATT
        self._attr_state_class = SensorStateClass.MEASUREMENT
