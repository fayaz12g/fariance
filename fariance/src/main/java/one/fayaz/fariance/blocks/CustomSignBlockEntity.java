package one.fayaz.fariance.blocks;

import net.minecraft.core.BlockPos;
import net.minecraft.world.level.block.entity.BlockEntity;
import net.minecraft.world.level.block.state.BlockState;

import net.minecraft.core.BlockPos;
import net.minecraft.world.level.block.entity.SignBlockEntity;
import net.minecraft.world.level.block.state.BlockState;

public class CustomSignBlockEntity extends SignBlockEntity {

    // Constructor matching the parent class
    public CustomSignBlockEntity(BlockPos pos, BlockState state) {
        super(pos, state); // Calls the SignBlockEntity constructor
    }

}
