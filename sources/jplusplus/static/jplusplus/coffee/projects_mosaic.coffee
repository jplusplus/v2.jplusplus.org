window.jplusplus = {} if not window.jplusplus

class window.jplusplus.Mosaïc

	constructor: (scope, plugin_instance=undefined) ->
		that = this
		# bind ui elements
		@ui  = $(scope)
		@uis = {
			projects_list : $(".projects"        , @ui)
			project_tmpl  : $(".project.template", @ui)
			filters       : $(".filter"          , @ui)
		}
		# load data
		$.getJSON("/api/v1/projects/?plugin_instance=#{plugin_instance}", @onDataLoaded)
		# bind events
		@uis.filters.click (e) ->
			that.onFilterSelected($(this).data('filter'))

	relayout: =>
		that  = this
		width = @ui.width()
		thumbnail_width    = 250
		thumbnail_height   = 100
		thumbnail_margin   = 40
		row_margin         = 50
		thumbnails_number  = $(".project:not(.template)", @ui).length
		thumbnails_per_row = Math.floor(width             / (thumbnail_width + thumbnail_margin))
		rows_number        = Math.ceil(thumbnails_number  / thumbnails_per_row)
		# size
		@uis.projects_list.css
			height: rows_number * (thumbnail_height + row_margin)
		$(".project:not(.template) .illustration").css
			width  : thumbnail_width
			height : thumbnail_height
		# position
		$(".project:not(.template)", @ui).each (i) ->
			nui = $(this)
			nui.css
				width : thumbnail_width
				top   : Math.floor(i / thumbnails_per_row) * (thumbnail_height + row_margin)
				left  : (i % thumbnails_per_row)           * (thumbnail_width  + thumbnail_margin)

	onDataLoaded: (data) =>
		# set size of elements
		for project in data
			nui = @uis.project_tmpl.clone().removeClass("template")
			image_url = project.image
			nui.find(".illustration").css
				"background-image" : "url(#{image_url})"
			nui.find(".title").html(project.title)
			@uis.projects_list.append(nui)
		@relayout()

	onFilterSelected: (filter) =>
		console.log "filter", filter

# EOF
