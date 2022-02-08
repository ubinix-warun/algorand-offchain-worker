from pyteal import *

def approval_program():
    ocw_state = Bytes("state")

    on_create = Seq(
        App.globalPut(ocw_state, Bytes("IDLE")),
        Approve(),
    )

    program = Cond(
        [Txn.application_id() == Int(0), on_create],
        [
            Or(
                Txn.on_completion() == OnComplete.OptIn,
                Txn.on_completion() == OnComplete.CloseOut,
                Txn.on_completion() == OnComplete.UpdateApplication,
            ),
            Reject(),
        ],
    )

    return program

def clear_state_program():
    return Approve()

if __name__ == "__main__":
    with open("offchain_approval.teal", "w") as f:
        compiled = compileTeal(approval_program(), mode=Mode.Application, version=5)
        f.write(compiled)

    with open("offchain_clear_state.teal", "w") as f:
        compiled = compileTeal(clear_state_program(), mode=Mode.Application, version=5)
        f.write(compiled)