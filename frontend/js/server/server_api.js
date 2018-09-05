const zerorpc = require("zerorpc")

let server = new zerorpc.Server({
    // Typical functions to use
    with_reply: function(arg, reply) {
        reply(null, 'You send: ' + arg);
        alert('with_reply');
    },
    empty: function(reply) {
        reply();
        alert('empty');
    },
    emit_event: function(reply) {
        reply();
        eventEmitter.emit('server_event');        
    },

    // Real example
    update_event: function(reply) {
        reply();
        eventEmitter.emit('server_update_event');        
    }
});