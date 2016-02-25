"""
 *  PROTECTION ENGINEERING CONSULTANTS CONFIDENTIAL
 *
 *  [2014] - [2015] Protection Engineering Consultants
 *  All Rights Reserved.
 *
 * NOTICE:  All information contained herein is, and remains
 * the property of Protection Engineering Consultants and its suppliers,
 * if any.  The intellectual and technical concepts contained
 * herein are proprietary to Protection Engineering Consultants
 * and its suppliers and may be covered by U.S. and Foreign Patents,
 * patents in process, and are protected by trade secret or copyright law.
 * Dissemination of this information or reproduction of this material
 * is strictly forbidden unless prior written permission is obtained
 * from Protection Engineering Consultants.
"""

__author__ = 'jbui'


# UNITY_VALUE = 'tnt'
FACTOR_CHARGE_ANFO = 0.82
FACTOR_CHARGE_COMPOSITION_A3 = 1.09
FACTOR_CHARGE_COMPOSITION_B = 1.11
FACTOR_CHARGE_COMPOSITION_C4 = 1.37
FACTOR_CHARGE_CYCLOTOL = 1.14
FACTOR_CHARGE_HBX_1 = 1.17
FACTOR_CHARGE_HBX_3 = 1.14
FACTOR_CHARGE_H6 = 1.38
FACTOR_CHARGE_MINOL_II = 1.20
FACTOR_CHARGE_OCTOL = 1.06
FACTOR_CHARGE_PBX_9404 = 1.13
FACTOR_CHARGE_PBX_9010 = 1.29
FACTOR_CHARGE_PETN = 1.27
FACTOR_CHARGE_PENTOLITE = 1.42
FACTOR_CHARGE_PICRATOL = 0.90
FACTOR_CHARGE_TETRYL = 1.07
FACTOR_CHARGE_TETRYTOL = 1.06
FACTOR_CHARGE_TNETB = 1.36
FACTOR_CHARGE_TNT = 1.0
FACTOR_CHARGE_TRITONAL = 1.07


CHARGE_KEY = {
    'ANFO': FACTOR_CHARGE_ANFO,
    'Composition A-3': FACTOR_CHARGE_COMPOSITION_A3,
    'Composition B': FACTOR_CHARGE_COMPOSITION_B,
    'Cyclotol (70/30)': FACTOR_CHARGE_CYCLOTOL,
    'HBX-1': FACTOR_CHARGE_HBX_1,
    'HBX-3': FACTOR_CHARGE_HBX_3,
    'H-6': FACTOR_CHARGE_H6,
    'Minoi II': FACTOR_CHARGE_MINOL_II,
    'Octol (70/30)': FACTOR_CHARGE_OCTOL,
    'PBX-9404': FACTOR_CHARGE_PBX_9404,
    'PBX-9010': FACTOR_CHARGE_PBX_9010,
    'PETN': FACTOR_CHARGE_PETN,
    'Pentolite': FACTOR_CHARGE_PENTOLITE,
    'Picratol': FACTOR_CHARGE_PICRATOL,
    'Tetryl': FACTOR_CHARGE_TETRYL,
    'Tetrytol': FACTOR_CHARGE_TETRYTOL,
    'TNETB': FACTOR_CHARGE_TNETB,
    'TNT': FACTOR_CHARGE_TNT,
    'tnt': FACTOR_CHARGE_TNT,
    'TRITONAL': FACTOR_CHARGE_TRITONAL,
}

DEFAULT_CHARGE_LIST = [
    'ANFO',
    'TNT',
    'TRITONAL'
]


def get_charge_conversion_factor(origin, destination):
    origin_factor = CHARGE_KEY.get(origin)
    destination_factor = CHARGE_KEY.get(destination)

    return destination_factor / origin_factor