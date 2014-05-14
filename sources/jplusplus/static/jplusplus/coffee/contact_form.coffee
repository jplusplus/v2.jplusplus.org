#!/usr/bin/coffee
# Encoding: utf-8
# -----------------------------------------------------------------------------
# Project : Journalism++ v2
# -----------------------------------------------------------------------------
# Author : Edouard Richard                                  <edou4rd@gmail.com>
# -----------------------------------------------------------------------------
# License : proprietary journalism++
# -----------------------------------------------------------------------------
# Creation : 04-May-2014
# Last mod : 04-May-2014
# -----------------------------------------------------------------------------
window.jplusplus = {} if not window.jplusplus

class window.jplusplus.ContactForm

	constructor: (scope) ->
		@ui  = $(scope)
		@uis =
			form           : $("form", @ui)
			successMessage : $(".success-message", @ui)
			errorMessage   : $(".error-message", @ui)
			backToFormBtn  : $(".success-message a, .error-message a", @ui)
			submitBtn      : $('.nl-submit', @ui)

		new NLForm(@uis.form.get(0))
		# bind event
		@uis.submitBtn.on("click", @onSubmitClick)
		@uis.backToFormBtn.on("click", @backToForm)

	onSubmitClick: (e) =>
		email = _.find(@uis.form.serializeArray(), (obj) -> obj.name=="email").value
		if not email? or email == ""
			@showErrorMessage()
		else
			$.ajax
				url      : @uis.form.attr("action")
				type     : "post"
				data     : @uis.form.serialize()
				dataType : "json"
				success  : (response) =>
					# fix he height of the element before removing content
					@ui.css('min-height', @ui.outerHeight(true))
					@uis.successMessage.removeClass("hidden")
					@uis.form.addClass("hidden")
				error: (xhr, ajaxOptions, thrownError) =>
					# response = jQuery.parseJSON(xhr.responseText)
					@showErrorMessage()
		# prevent the page reload
		e.preventDefault()
		return false

	showErrorMessage: () =>
		@ui.css('min-height', @ui.outerHeight(true))
		@uis.errorMessage.removeClass("hidden")
		@uis.form.addClass("hidden")

	backToForm: (e) =>
		# reset dynamic height
		@ui.css('min-height', '')
		@uis.successMessage.addClass("hidden")
		@uis.errorMessage.addClass("hidden")
		@uis.form.removeClass("hidden")
		e.preventDefault()
		return false

# EOF
