
class Mosaïc

	constructor: (scope, plugin_instance=undefined) ->
		# bind ui elements
		@ui  = $(scope)
		@uis = {
			project_tmpl : $(".project.template", @ui)
		}
		# load data
		$.getJSON("/api/v1/projects/?plugin_instance=#{plugin_instance}", @onDataLoaded)

	onDataLoaded: (data) =>
		for project in data
			nui = @uis.project_tmpl.clone().removeClass("template")
			image_url = project.image
			nui.find(".illustration").css
				"background-image" : "url(#{image_url})"
			nui.find(".title").html(project.title)
			@ui.append(nui)

# EOF

