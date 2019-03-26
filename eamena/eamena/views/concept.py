'''
ARCHES - a program developed to inventory and manage immovable cultural heritage.
Copyright (C) 2013 J. Paul Getty Trust and World Monuments Fund

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
'''

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required, user_passes_test
from arches.app.views.concept import rdm as core_rdm
from arches.app.views.concept import concept as core_concept

# Wrap the core views for rdm and concept in new views with slightly stricter
# permissions ("editplus" membership, not just edit).

@user_passes_test(lambda u: u.groups.filter(name='editplus').count() != 0, login_url='/auth/')
def rdm(request, conceptid):

    return core_rdm(request, conceptid)

@csrf_exempt
@user_passes_test(lambda u: u.groups.filter(name='editplus').count() != 0, login_url='/auth/')
def concept(request, conceptid):

    return core_concept(request, conceptid)
