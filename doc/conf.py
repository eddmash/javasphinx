#
# Copyright 2012-2015 Bronto Software, Inc. and contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

project = 'javasphinx'
version = '0.9.14'
release = '0.9.14'

extensions = ['javasphinx']

master_doc = 'index'
copyright = u'2012-2015, Bronto Software Inc. and contributors'

pygments_style = 'tango'

html_theme = 'nature'
html_short_title = project
html_sidebars = {'**' : ['localtoc.html', 'relations.html', 'sourcelink.html']}

primary_domain = 'rst'
