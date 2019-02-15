define(['jquery', 'backbone', 'arches', 'views/concept-search', 'models/concept'], function ($, Backbone, arches, ConceptSearch, ConceptModel) {
    return ConceptSearch.extend({

        events: {
            'click .modal-footer .savebtn': 'save'
        },

        initialize: function(){
            ConceptSearch.prototype.initialize.apply(this, arguments);
            this.modal = this.$el.find('.modal');
            this.relationshiptype = this.modal.find('#related-relation-type').select2({
                minimumResultsForSearch: 10,
                maximumSelectionSize: 1
            });
        },
        
        save: function(){
            var self = this;
            if (this.searchbox.val() !== ''){
                if (this.searchbox.val() === $("#parentconceptid").val()) {
                    $("#invalidvalue").show(0).delay(4000).hide(0);
                } else {
                    var relatedConcept = new ConceptModel({
                        id: this.searchbox.val(),
                        relationshiptype: this.relationshiptype.val()
                    });
                    this.model.set('relatedconcepts', [relatedConcept]);
    
                    this.modal.on('hidden.bs.modal', function (e) {
                        self.model.save();
                    })
                    this.modal.modal('hide');                    
                }
            }
        }
    });
});