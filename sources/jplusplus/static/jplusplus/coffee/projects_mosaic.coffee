#!/usr/bin/coffee
# Encoding: utf-8
# -----------------------------------------------------------------------------
# Project : Journalism++ v2
# -----------------------------------------------------------------------------
# Author : Edouard Richard                                  <edou4rd@gmail.com>
# -----------------------------------------------------------------------------
# License : proprietary journalism++
# -----------------------------------------------------------------------------
# Creation : 23-Apr-2014
# Last mod : 23-Apr-2014
# -----------------------------------------------------------------------------
window.jplusplus = {} if not window.jplusplus

class window.jplusplus.Mosaïc
	
	CONFIG = 
		thumbnails_per_row : 4
		thumbnail_min_width: 100
		thumbnail_margin   : 20
		row_margin         : 60
		image_ratio        : 1.666

	constructor: (scope, plugin_instance=undefined) ->
		that    = this
		@config = CONFIG
		# bind ui elements
		@ui  = $(scope)
		@uis = {
			projects_list : $(".projects"        , @ui)
			project_tmpl  : $(".project.template", @ui)
			filters       : $(".filter"          , @ui)
		}
		@data     = [] # all project objects
		@projects = [] # list of {nui:$(), slug:""} shown on layout
		# load data
		url = "/api/v1/projects/"
		url += "?plugin_instance=#{plugin_instance}" if plugin_instance
		$.getJSON(url, @onDataLoaded)
		# bind events
		@uis.filters.click (e) ->
			that.onFilterSelected($(this).data('filter'))
		$(window).resize(_.debounce(@relayout, 500))

	relayout: =>
		that  = this
		width = @ui.width()
		thumbnails_number  = $(".project:not(.template)", @ui).length
		thumbnails_per_row = @config.thumbnails_per_row
		thumbnail_margin   = @config.thumbnail_margin
		thumbnail_width    = (width / thumbnails_per_row) - thumbnail_margin
		if thumbnail_width < @config.thumbnail_min_width
			thumbnails_per_row -= 1
			thumbnail_width = 100
		thumbnail_height   = thumbnail_width / @config.image_ratio
		row_margin         = @config.row_margin
		# thumbnails_per_row = Math.floor(width             / (thumbnail_width + thumbnail_margin))
		rows_number        = Math.ceil(thumbnails_number  / thumbnails_per_row)
		# size
		new_widget_height  = rows_number * (thumbnail_height + row_margin)
		# only if new size is greater than the previous
		if parseFloat(@uis.projects_list.css("height").replace("px", "")) < new_widget_height
			@uis.projects_list.css
				height: new_widget_height
			$(document).trigger("heightHasChanged")
		$(".project:not(.template) .frame").css
			width  : thumbnail_width
			height : thumbnail_height
		# position
		for project, i in @projects
			if project?
				project.nui.css
					width : thumbnail_width
					top   : Math.floor(i / thumbnails_per_row) * (thumbnail_height + row_margin)
					left  : (i % thumbnails_per_row)           * (thumbnail_width  + thumbnail_margin)

	onDataLoaded: (data) =>
		# set size of elements
		@data = data
		@showProjects(@data)

	showProjects: (projects) =>
		# removing older projects
		for project, i in @projects
			project.nui.remove() if project? and not _.findWhere(projects, {"slug" : project.slug})?	
		# add new projects
		new_projects_mapping = []
		for project, i in projects
			# recycling project nui if exists
			old_project = _.find(@projects, (e) -> e.slug == project.slug)
			if old_project
				nui = old_project.nui
			else
				nui = @uis.project_tmpl.clone().removeClass("template")
				image_url = project.image
				nui.find(".illustration").css
					"background-image" : "url(#{image_url})"
				nui.find(".title").html(project.title)
				nui.find("a").attr("href", project.url)
				# add to view
				@uis.projects_list.append(nui)
			new_projects_mapping.push({slug: project.slug, nui:nui})
		@projects = new_projects_mapping
		@relayout()

	onFilterSelected: (filter) =>
		#select the filter on screen
		@uis.filters.removeClass("active")
		@uis.filters.filter("[data-filter=#{filter}]").addClass("active")
		# show relative projects
		if filter == "all"
			@showProjects(@data)
		else
			@showProjects(@data.filter((e) -> filter in e.tags))		

# EOF
