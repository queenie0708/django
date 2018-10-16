 <script language="javascript">
       $("#Project").change(function()
     {
        var optionSelected = $("option:selected", this);
        var dut_id = this.value;
       $.ajax({
                           url: '/ajax/load_versions/',
                           data: {
                                    'dut_id': dut_id,
                                    //'csrfmiddlewaretoken': '{{ csrf_token }}'
                                  },
                           type: 'GET',
                           dataType: 'json',
                           success: function (version)
						   {
                               var obj = JSON.parse(version)
                                var version_json = JSON.parse(obj)
                                $('#Version').empty();
                                for (i in version_json) {
                                  $('#Version').append($("<option></option>")
                                                  .attr("value", version_json[i].sw_version+"|"+version_json[i].lastupdate)
                                                  .text(version_json[i].sw_version+"|"+version_json[i].lastupdate));
								}

						   },

               });
     });

      $("#Version").change(function()
     {
        var optionSelected = $("option:selected", this);
        var sw_build = this.value;
        var  build= sw_build.split("|");
        var sw_version =build[0];
        $('#build td:(eq0)').text(sw_version);
        $('#build +tr').text(build[1]);

       $.ajax({
                           url: '/ajax/load_results/',
                           data: {
                                    'sw_version': sw_version,
                                    //'csrfmiddlewaretoken': '{{ csrf_token }}'

                                  },
                           type: 'GET',
                           dataType: 'json',
                           success: function (result)
						   {
                                var obj = JSON.parse(result)
                                var result_json = JSON.parse(obj)
                                for (var i=0;i<result_json.length;i++) {

                                  $('#result').append($("<tr></tr>")
                                                  .attr("value", [i])
                                                  .text(result_json[i].test_description));
								}



						   },

               });
     });

 </script>

